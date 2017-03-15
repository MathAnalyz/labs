<?php
// web/index.php
require_once __DIR__.'/../vendor/autoload.php';
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

Request::enableHttpMethodParameterOverride();

$app = new Silex\Application();
$app['debug'] = true;
$app->register(new Silex\Provider\TwigServiceProvider(),
        ['twig.path' => __DIR__ . '/../view']);
$app->register(new Silex\Provider\DoctrineServiceProvider(),
        ['db.options' => ['driver' => 'pdo_mysql', 'dbname' => 'hw_php', 'charset' => 'utf8']]);
		
$app->get('/', function () use ($app) {
    /**@var $conn Connection */
    $conn = $app['db'];
    $students = $conn->fetchAll('select * from students');
    return $app['twig']->render('students.twig', ['students' => $students]);
});

$app->get('/students/{id}', function ($id) use ($app) {
    /**@var $conn Connection */
    $conn = $app['db'];
    $student = $conn->fetchAssoc('select * from students where id = ?', [$id]);
    if (!$student) {
        throw new NotFoundHttpException("Нет такого студента - $id");
    }
    $subjects = $conn->fetchAll('select * from subjects');
    $scores = $conn->fetchAll('select * from scores where student_id = ?', [$id]);
    $scorez = [];
    foreach ($scores as $score) {
        $scorez[$score['subject_id']] = $score['score'];
    }
    return $app['twig']->render('student.twig', ['student' => $student, 'subjects' => $subjects, 'scorez' => $scorez]);
});

$app->post('/students', function (Request $req) use ($app) {
	/**@var $conn Connection */
	$conn = $app['db'];
	$name = $req->get('name');
	$conn->insert('students', ['name' => $name]);
	return $app->redirect('/');
});

$app->delete('/students/{id}', function ($id) use ($app) {
    /**@var $conn Connection */
    $conn = $app['db'];
    $conn->delete('students', ['id' => $id]);
    return $app->redirect('/');
});

$app->put('/students/{id}/scores', function (Request $req, $id) use ($app) {
    /**@var $conn Connection */
    $conn = $app['db'];
    $conn->transactional(function (Doctrine\DBAL\Connection $conn) use ($id, $req) {
        $conn->delete('scores', ['student_id' => $id]);
        foreach ($req->get('scores') as $subject_id => $score) {
            if ($score) {
                $conn->insert('scores', ['student_id' => $id, 'subject_id' => $subject_id, 'score' => $score]);
            }
        }
    });
    return $app->redirect("/students/$id");
});

$app->run();