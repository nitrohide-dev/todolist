function Queue() {
  this.elements = [];
}

Queue.prototype.enqueue = function (element) {
  this.elements.push(element);
};

Queue.prototype.dequeue = function () {
  return this.elements.shift();
};

Queue.prototype.peekLast = function(){
    return this.elements[0];
}

function addToQueue() {
    event.preventDefault();
  queue.enqueue(task.value);
  task.value = '';
  p1.innerHTML = queue.peekLast();
}
function removeFromQueue(){
    p1.innerHTML = queue.dequeue();
    

}


let queue = new Queue();
let task = document.getElementById('task');
let paragraph = document.getElementById("p1")

