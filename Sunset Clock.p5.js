function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
  
}

function draw() {
  background(150);
  translate(200,200);
  rotate(-90);
  
  let hr = hour();
  let min = minute();
  let sec = second();
  
  strokeWeight(4);
  stroke(0);
  noFill();
  //ellipse(200,200,300,300);
  
  stroke(255, 100, 100);
  
  let end = map(sec, 0, 60, 0, 360);
  arc(0,0,300,300,0,end);
  
  stroke(255, 180, 80);  
  let end2 = map(min, 0, 60, 0, 360);
  arc(0,0,250,250,0,end2);
  
  stroke(255);  
  let end3 = map(hr % 12, 0, 12, 0, 360);
  arc(0,0,200,200,0,end3);
  
 fill(0);
	rotate(90);
 noStroke();
 textSize(18);
  
  let time = text(hr + ':' + min + ':' + sec, -35,10);
  
}
