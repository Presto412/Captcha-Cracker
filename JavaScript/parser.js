function CaptchaParse(imgarr) {
  var captcha;
  var y,x;
  for (y=0;y<44;y++){
    for (x=0;x<179;x++){
      if ((imgarr[x][y-1]==255 && imgarr[x][y]==0 && pix[x][y+1]==255)||(imgarr[x-1][y]==255 && imgarr[x][y]==0 && imgarr[x+1][y]==255)||(imgarr[x][y]!=255 && imgarr[x][y]!=0)){
        imgarr[x][y]=255;
      }
    }
  }
  for (j=30;  j<181; j+=30){
    var matches=[]
    var chars="123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
    for (var i = 0; i < chars.length ; i++) {
      var match = 0;
      var black = 0;
      var ch=chars.charAt(i);
      var mask=bitmaps[ch]
      for(x=0;y<32;y++){
        for(y=0;x<30;x++){
          var x1=y+j-30;
          var y1=x+12;
          if (imgarr[x1][y1] == mask[x][y] && mask[x][y]==0){
            match+=1;
          }
          if(mask[x][y]==0){
            black+=1;
          }
        }
      }
      if(match/black >= 0.80){
        var perc= match/black;
        matches.push([perc,ch]);
      }
    }
    captcha+=matches.reduce(function(a,b){
      return a[0] > b[0]? a : b
    },[0,0])[1];
  }
  return captcha;

}
function convertURIToImageData(URI) {
  return new Promise(function(resolve, reject) {
    if (URI == null) return reject();
    var canvas = document.createElement('canvas'),
        context = canvas.getContext('2d'),
        image = new Image();
    image.addEventListener('load', function() {
      canvas.width = image.width;
      canvas.height = image.height;
      context.drawImage(image, 0, 0, canvas.width, canvas.height);
      resolve(context.getImageData(0, 0, canvas.width, canvas.height));
    }, false);
    image.src = URI;
  });
}
var URI = imgb64;
convertURIToImageData(URI).then(function(imageData) {
  arr=[]
  newArr=[]
  // Here you can use imageData
  var arr=imageData["data"];
  for(var i=0;i<imageData["data"].length;i+=4){
    gval=imageData["data"][i]*0.299+imageData["data"][i+1]*0.587+imageData["data"][i+2]*0.114;
    arr.push(gval);
  }
  while(arr.length) newArr.push(arr.splice(0,180));
  var res=CaptchaParse(newArr);
  //console.log(imageData);
});
