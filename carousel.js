(function(){
  var car=document.getElementById('car'); if(!car) return;
  var track=car.querySelector('.track'), dots=[].slice.call(car.querySelectorAll('.dots button')), n=dots.length, i=0, t;
  function go(k){i=(k+n)%n;track.style.transform='translateX('+(-100*i)+'%)';dots.forEach(function(d,j){d.classList.toggle('on',j===i)});}
  function play(){clearInterval(t);t=setInterval(function(){go(i+1)},4000);}
  car.querySelector('.prev').onclick=function(){go(i-1);play()};
  car.querySelector('.next').onclick=function(){go(i+1);play()};
  dots.forEach(function(d,j){d.onclick=function(){go(j);play()}});
  var x=null;car.addEventListener('touchstart',function(e){x=e.touches[0].clientX},{passive:true});
  car.addEventListener('touchend',function(e){if(x===null)return;var d=e.changedTouches[0].clientX-x;if(Math.abs(d)>40){go(i+(d<0?1:-1));play()}x=null});
  car.addEventListener('mouseenter',function(){clearInterval(t)});car.addEventListener('mouseleave',play);
  go(0);play();
})();
