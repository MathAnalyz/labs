// ����������� ����������� ����������: ��������� express
var express = require('express'),
    // ��������� ������� HTML � JSON ��� ����, 
    // ���������: � ��������� �� ����� expressjs.com
    bodyParser = require('body-parser'),
    // ���������� mongoose ��� ����� ��������
    // �������������� � ��
    mongoose = require('mongoose'),
    // � ����� ��� �������� ����� ��
    dbSchema = mongoose.Schema,
	// ������������...
    swig = require('twig'),
	// �, ����������, ����� ����������
	app = express();
	
// �� ����� public ����� �������� �������: ����� � ������� ��� ���������
app.use(express.static(__dirname + '/public'));
// ������������ � �������� mongoDB
mongoose.connect('mongodb://localhost/plantsdb', function (err, db) {
		
	// ��������� ����� ���������� � ��������� mongoDB
	// ������. ����� �������, ����� �������� � nosql
	// ����� � ��������� �����
	var plantsSchema = new dbSchema({
		rus_name:  String,
		lat_name:  String,
		info:  String,
		sec_measures:  String,
		status_p:  Number,
		division: Number,
		reservations: [{String}]
	});
	
	var divisionSchema = new dbSchema({
		_id: Number,
		name: String,
		annotation: String
	});
	
	var statusSchema = new dbSchema({
		_id: Number,
		name: String,
		info: String
	});
	
	var rsvSchema = new dbSchema({
		_id: Number,
		name: String,
	});

	// ������� ������ �� �����, �������� �� ��������� 'plants'
	var PlantsModel = mongoose.model('plants', plantsSchema);
	var StatusModel = mongoose.model('statuses', statusSchema);
	var DivisionModel = mongoose.model('divisions', divisionSchema);
	var ReservationModel = mongoose.model('reservations', rsvSchema);

	// ��������� ������� � ���������������
	app.set('views', __dirname + '/views');

	// ���������� body-parser ��� ��������� ��������
	app.use(bodyParser.urlencoded({ extended: true }));
	app.use(bodyParser.json());;
	
	//������ ������� ��������
	app.get('/', function(req, res) {
		DivisionModel.find({}).exec(function(err, divisions) {
			res.render('index.twig', {
				divisions: divisions
			});
		});
	});
	
	app.get('/division/:id', function(req, res) {
		DivisionModel.find({}).exec(function(err, divisions) {
			StatusModel.find({}).exec(function(err, statuses) {
				ReservationModel.find({}).exec(function(err, reservations) {
					DivisionModel.findOne({ "_id": { $eq: req.params.id }}).exec(function(err, cur_division) {
						PlantsModel.find({ "division": { $eq: req.params.id }}).exec(function(err, ps) {
							console.log("%j", req.params.id);
							res.render('plants_in_division.twig', {
								// ������������� � ������������� ����������� ����������
								plants: ps,
								dvs: cur_division,
								divisions: divisions,
								reservations: reservations,
								statuses: statuses
							});
						});
					});
				});
			});
		});
	});
	
	app.post('/division/:id_d/plant', function(req, res) {
		console.log("%j", req.body.reservation);
		StatusModel.findOne({"name": { $eq: ""+req.body.status}}).exec(function (err, selected_status) {
			var s = new PlantsModel({ 
				rus_name:  req.body.rus_name,
				lat_name:  req.body.lat_name,
				info:  req.body.info,
				sec_measures:  req.body.sec_measures,
				status_p:  selected_status._id,
				division: req.params.id_d,
				reservations: []
			});
			console.log("%j", s);
			s.save(function (err) {
				if (err) return handleError(err);
				res.redirect('/division/' + req.params.id_d);
			});
		});
	});	

	app.get('/division/:id_d/plant/:id_p', function(req, res) {
		DivisionModel.find({}).exec(function(err, divisions) {
			StatusModel.find({}).exec(function(err, statuses) {
				ReservationModel.find({}).exec(function(err, reservations) {
					PlantsModel.findOne({ "_id": { $eq: req.params.id_p }}).exec(function(err, ps) {
						res.render('edit_plant.twig', {
							// ������������� � ������������� ����������� ����������
							plant: ps,
							dvs: req.params.id_d,
							divisions: divisions,
							reservations: reservations,
							statuses: statuses
						});
					});
				});
			});
		});	
	});
	
	
	app.post('/division/:id_d/plant/:id_p/put', function(req, res) {
		StatusModel.findOne({"name": { $eq: ""+req.body.status}}).exec(function (err, selected_status) {
			PlantsModel.findOne({"_id": { $eq: req.params.id_p}}).exec(function (err, plant) {
				PlantsModel.updateOne(
					{ "_id" :  plant._id},
					{ 	$set: {
							rus_name:  req.body.rus_name,
							lat_name:  req.body.lat_name,
							info:  req.body.info,
							sec_measures:  req.body.sec_measures,
							status_p:  selected_status._id,
							division: req.params.id_d,
							reservations: []
						} 
				}).exec(function (err) {
					res.redirect('/division/' + req.params.id_d);
				});
			});
		});
	});
	
	/*
	app.post('/division/:id_d/plant/:id_p/put', function(req, res) {
		StatusModel.findOne({"name": { $eq: ""+req.body.status}}).exec(function (err, selected_status) {
			var plant = new plantsSchema({
				rus_name:  req.body.rus_name,
				lat_name:  req.body.lat_name,
				info:  req.body.info,
				sec_measures:  req.body.sec_measures,
				status_p:  selected_status._id,
				division: req.params.id_d,
				reservations: []
			});
			var upsertData = plant.toObject();
			delete upsertData._id;
			return plantsSchema.update({_id: req.params.id_p}, upsertData, {upsert: false}, function (err) {
				if (err) return handleError(err);
				res.redirect('/division/'+req.params.id_d);
			});
		});
	});
	
	*/
	
	app.post('/division/:id_d/plant/:id_p/delete', function(req, res) {
		PlantsModel.findOneAndRemove({_id: req.params.id_p}, function (err) {
            if (err) return handleError(err);
            res.redirect('/division/'+ req.params.id_d);
        });
	});
	
	//������ ������ �� ����, ������� ��� ����������
	app.listen(8082);
	console.log('Express server listening on port 8082');
});