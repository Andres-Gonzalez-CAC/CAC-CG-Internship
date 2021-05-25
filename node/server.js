var https = require ('https');
var fs = require('fs');
var url = require('url');

const options = {
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('server.crt')
};
var server = https.createServer(options,(req,res)=>{
    // var path = req.path;
    // if(path == '/popup.html'){

        fs.readFile('popup.php',(err,data)=>{
            if(err){
                console.log(err);
                res.end()
            } else{
                res.write(data);
                res.end();
            }
        });
    // }
});

server.listen(5000)