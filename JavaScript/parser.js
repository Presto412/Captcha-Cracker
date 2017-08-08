function CaptchaParse(imgb64) {
  //add code to read base64
  //add code to convert to grayscale
  //imgarr is 2d array of image
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
