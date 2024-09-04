const EventEmitter = require('events'); //class
//const emitter = new EventEmitter(); Don't need this

//Let's say we are logging stuff to the cloud
//Through a url endpoint
var url = 'https://mylogger.io/log';

//Define class so we can extend emitter
class Logger extends EventEmitter {
    /*Don't need to write "function"*/ log(message) {
        //Send HTTP request
        console.log(message);
    
        //Logger module emits an event
        //Raise an event
        //Can use this for EventEmitter, instead 
        //of emitter
        this.emit('messageLogged');
        this.emit('messageLogged', {id: 3, url: 'https://'})
    
    }
}


module.exports.logger = Logger;
module.exports.happy = true;

