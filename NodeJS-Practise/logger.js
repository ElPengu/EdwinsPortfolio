//Let's say we are logging stuff to the cloud
//Through a url endpoint
var url = 'https://mylogger.io/log';

function log(message) {
    //Send HTTP request
    console.log(message);
}

module.exports.logger = log;
module.exports.happy = true;

