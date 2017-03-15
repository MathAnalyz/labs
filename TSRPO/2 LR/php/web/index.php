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
        ['db.options' => ['driver' => 'pdo_mysql', 'dbname' => 'plants', 'charset' => 'utf8']]);
$app->get('/', function () use ($app) {
    /**@var $conn Connection */
    $conn = $app['db'];
    $division = $conn->fetchAll('select * from division');
	return $app['twig']->render('index.twig', ['division' => $division]);
});
$app->get('/division/{id}', function ($id) use ($app) {
    /**@var $conn Connection */
    $conn = $app['db'];
    $division = $conn->fetchAll('select * from division');
    $plants = $conn->fetchAll('select * from plants_table where division = ?', [$id]);
	$reservation = $conn->fetchAll('select * from reservation');
	$status = $conn->fetchAll('select * from status');
	$pl_rsrvtn = $conn->fetchAll('select * from plants_reservation');
	$dvs = $conn->fetchAssoc('select * from division where id = ?', [$id]);
	return $app['twig']->render('plants_in_division.twig', ['plants' => $plants, 
															'dvs' => $dvs, 
															'division' => $division, 
															'status' => $status,
															'reservation' => $reservation,
															'pl_rsrvtn' => $pl_rsrvtn]);
});
$app->get('/division/{div}/plants/{id}', function (Request $req, $div, $id) use ($app) {
    $conn = $app['db'];
    $division = $conn->fetchAll('select * from division');
    $plant = $conn->fetchAssoc('select * from plants_table where id = ?', [$id]);
	$reservation = $conn->fetchAll('select * from reservation');
	$status = $conn->fetchAll('select * from status');
	$pl_rsrvtn = $conn->fetchAll('select * from plants_reservation');
	$dvs = $conn->fetchAssoc('select * from division where id = ?', [$plant["division"]]);
	return $app['twig']->render('edit_plant.twig', ['plant' => $plant, 
															'division' => $division,
															'dvs' => $dvs,  
															'status' => $status,
															'reservation' => $reservation,
															'pl_rsrvtn' => $pl_rsrvtn]);
});
$app->put('/division/{div}/plants/{id}', function (Request $req, $div, $id) use ($app) {
    $conn = $app['db'];
	$rus_name = $req->get('rus_name');
	$lat_name = $req->get('lat_name');
	$info = $req->get('info');
	$sec_measures = $req->get('sec_measures');
	$status = $req->get('status');
	$name_reservations = $req->get('reservation');
	$status_id = $conn->fetchAssoc('select id from status where name = ?', [$status]);
	$conn->update('plants_table', 
								['rus_name' => $rus_name,
								   'lat_name' => $lat_name,
								   'info' => $info,
								   'sec_measures' => $sec_measures,
								   'status_id' => $status_id["id"],],
								['id' => $id]);
	$pl_rsrvtn = $conn->fetchAll('select * from plants_reservation');
	foreach ($pl_rsrvtn as $key)
	{
		if ($key["plants_id"] == $id)
			$conn->delete('plants_reservation', ['id' => $key['id']]);
	}
	$rsrv_id = $conn->fetchAssoc('select id from reservation where name = ?', [$name_reservations]);
	if ($rsrv_id)
		$conn->insert('plants_reservation', ['plants_id' => $id, 'reservation_id' => $rsrv_id["id"]]);
    return $app->redirect("/division/".$div);
});
$app->post('/plants/{dvs_id}', function (Request $req, $dvs_id) use ($app) {
	$conn = $app['db'];
	$rus_name = $req->get('rus_name');
	$lat_name = $req->get('lat_name');
	$info = $req->get('info');
	$sec_measures = $req->get('sec_measures');
	$status = $req->get('status');
	$name_reservations = $req->get('reservation');
	$status_id = $conn->fetchAssoc('select id from status where name = ?', [$status]);
	$conn->insert('plants_table', ['rus_name' => $rus_name,
								   'lat_name' => $lat_name,
								   'info' => $info,
								   'sec_measures' => $sec_measures,
								   'status_id' => $status_id["id"],
								   'division' => $dvs_id]);
    $id = $conn->fetchAssoc('select id from plants_table where rus_name = ?', [$rus_name]);
	$rsrv_id = $conn->fetchAssoc('select id from reservation where name = ?', [$name_reservations]);
	//var_dump($rsrv_id);
	if ($rsrv_id)
		$conn->insert('plants_reservation', ['plants_id' => $id["id"], 'reservation_id' => $rsrv_id["id"]]);
	return $app->redirect('/division/'.$dvs_id);
});
$app->delete('/division/{div}/plants/{id}', function ($div, $id) use ($app) {
    $conn = $app['db'];
	$pl_rsrvtn = $conn->fetchAll('select * from plants_reservation');
	foreach ($pl_rsrvtn as $key)
	{
		if ($key["plants_id"] == $id)
			$conn->delete('plants_reservation', ['id' => $key['id']]);
	}
    $conn->delete('plants_table', ['id' => $id]);
    return $app->redirect('/division/'.$div["id"]);
});
$app->run();