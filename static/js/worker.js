self.addEventListener('message',function (e){
    // receive message from page.
    var message = e.data;
    // send message to page.
    self.postMessage(e.data + '-processed!');

});
self.postMessage('READY');
