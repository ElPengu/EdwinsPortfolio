function sayHello(name) {
    console.log(`Hello ${name}!`)
}

sayHello("Edwin");

//This fails, unlike in regular JS
//Nor document objects
//We can work with files and stuff though
//Just try see if this code works!
//console.log(window); 

//Modules we can work with
//OS - operating system
//fs - file system
//events
//http

//Global object - can be called anywhere
console.log();// console is a global object
//setTimeout(); //setTimeout is a global object, basically time.sleep

//setInterval(); // Calls function repeatedly after delay
//clearInterval(); //Stops setInterval calling function


//In browsers, window object is global scope
//Here though, we have global object instead
var message = "message";
console.log(global.message); //Will be undefined
//To scope to this file, we must add it to the 
//global scope

//But if we define two functions in same name 
//across files, one function overwrites the 
//other
//Every file is a module
//To avoid this, we must modularise objects and
//vars!
//console.log(module);


//Let us access the function in the logger 
//module
console.log("Let us access a function in logger.js");
//Use const so that we do not override!
const LoggerModule =  require('./logger'); //Put relative file path
const logger = LoggerModule.logger; //Accesses logger function
const happiness = LoggerModule.happiness; // Accessess happiness property
console.log(`logger: `, logger); //Doesn't work?

LoggerModule.logger("My message");

console.log("Done with logger.js for now");

console.log('');

console.log("We can even access file name and directory!");
console.log(`File name: ${__filename}`);
console.log(`Directory name: ${__dirname}`);
console.log(``);
const documentationPageOfModules = "https://nodejs.org/docs/latest/api/";
console.log(`Modules that can be used can be found on ${documentationPageOfModules}`)
console.log("Let us look at the path module");
const path = require('node:path');
var pathObj = path.parse(__filename);

console.log(`Path object on file name: `, pathObj);
console.log('');

console.log("Let us get some information on the OS using the os module");
const os = require('os');
const totalMemory = os.totalmem();
const freeMemory = os.freemem();
console.log(`Total memory: ${totalMemory}`);
console.log(`freeMemory: ${freeMemory}`);
console.log('');

console.log("Now we can take a look at the file system!");
const fs = require('fs');

//Every function in file system module comes in async and sync 
//versions. For apps, we use async version, although it is 
//a bit harder to write
//Sync version
//const files = fs.readdirSync('./');
//console.log("Files in home directory: " + files);
//Aync version
fs.readdir('./', function(err, files) {
    if (err) console.log('ASYNC readdir: Error', err);
    else console.log("ASYNC readdir: Files in home directory are: " + files);
});

console.log('');


//Events module
console.log('Now we look at the events module');
//Load in events module
const EventEmitter = require('events'); //class
const emitter = new EventEmitter; //Instance/object

//Register an listener
emitter.on('messageLogged', 
    /*Function called when raised*/function(arg){
        if (arg == null) console.log('Listener called without arguments');
        else console.log(`Listener called with id: ${arg.id}, url: ${arg.url}`);
        

})

emitter.emit('messageLogged', {id: 1, url: 'http://'});

//We get a class from loggerExtender
const LoggerExtenderModule = require('./loggerExtender');
const LoggerExtenderClass = LoggerExtenderModule.logger;
const loggerExtender = new LoggerExtenderClass();

//Register a listener for loggerExtender
loggerExtender.on('messageLogged', function(arg) {
    if (arg == null) {
        console.log('Listener called');
        console.log(`Message sent with no argument: ${message}`);
    } else {
        console.log('Listener called');
        console.log(`Message called: ${message}, id: ${arg.id}, url: ${arg.url}`)
    }
});
loggerExtender.log('message');
console.log('')



//But it is rare to work with the emitter object 
//directly. Often we extend it


//HTTP module
const http = require('node:http');

//We can create web server
//Server extends emit because it extends net.Server
const server = http.createServer();

server.on('connection', function (socket) {
    console.log('New connection');
});

//In real world, we won't respond to port,
//low level

const newServer = http.createServer(function(req, res) {
    
    if (req.url == '/') {
        res.write('Hello world');
        res.end();
    }

    if (req.url == '/api/courses') {
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});


//Listen on port 3000
server.listen(3000);

//Listening on port 3001
newServer.listen(3001);
console.log('Listening on port 3000');

console.log('');
console.log('');