const express = require('express')
const {spawn} = require('child_process');
const bodyParser = require("body-parser");
const app = express()
const port = process.env.PORT || 3000;
app.set("views", "./views");
app.set("view engine", "ejs");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded( { "extended" : true } ));
app.get('/', (req, res) => {
   /* const python = spawn('python', ['./py/knapsack-problem.py', 
    'Työasemat',6600,58400,
    'Huonekalut',3700,30000,
    'Mobiililaitteet',5700,58400,
    'Osuus vapaa- ajan mökistä',3200,50000,
    141700,
    ]);*/
    res.render("index", { "error" : "",
    "sisalto" : "", "hyoty" : "", "kustannus" : "",
    "name1":"","weight1":"","benefit1":"",
    "name2":"","weight2":"","benefit2":"",
    "name3":"","weight3":"","benefit3":"",
    "name4":"","weight4":"","benefit4":"", "budget":""});
 })

 app.post("/laske/", (req, res) => {
    let stringData;
    // spawn new child process to call the python script
    const python = spawn('python', ['./py/knapsack-problem.py', 
    req.body.name1,req.body.benefit1,req.body.weight1,
    req.body.name2,req.body.benefit2,req.body.weight2,
    req.body.name3,req.body.benefit3,req.body.weight3,
    req.body.name4,req.body.benefit4,req.body.weight4,
    req.body.budget,
]);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        stringData = data.toString()
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        eval('var obj='+stringData);

        // send data to browser
        if(obj&&stringData){
           res.render("index", { "error" : "", 
            "sisalto" : obj.sisalto, "hyoty" : obj.kokonaishyoty, "kustannus" : obj.kokonaiskustannus,
            "name1":req.body.name1,"benefit1":req.body.benefit1,"weight1":req.body.weight1,
            "name2":req.body.name2,"benefit2":req.body.benefit2,"weight2":req.body.weight2,
            "name3":req.body.name3,"benefit3":req.body.benefit3,"weight3":req.body.weight3,
            "name4":req.body.name4,"benefit4":req.body.benefit4,"weight4":req.body.weight4,
             "budget":req.body.budget });
        } else { 
           res.render("index", { "error" : `Tapahtui virhe! Virhekoodi ${code}`, 
           "sisalto" : "", "hyoty" : "", "kustannus" : "",
           "name1":"","weight1":"","benefit1":"",
           "name2":"","weight2":"","benefit2":"",
           "name3":"","weight3":"","benefit3":"",
           "name4":"","weight4":"","benefit4":"", "budget":"" });
        }
    })
 })
app.listen(port, () => console.log(`Node app listening on port ${port}!`))