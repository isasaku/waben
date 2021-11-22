let today=new Date(); 
let month=today.month;
let year=today.year;
let mon=month+1;
let date=new Date(year,mon,0);
let len=date.getDate();
const yob=["日","月","火","水","木","金","土"];
for(let i=0; i< len; i++){     
   let id="d"+i;
   let yobNo=new Date(year,month,i).getDay()
   document.querySelector(id).innerHTML = yob[yobNo];
}
