  Name       Size            Bytes  Class     Attributes

  Fs         1x1                 8  double              
  ans        1x1                 8  double              
  x         80x1               640  double              
  y         13x1               104  double              

plot(x)
y = diff(x);
min(abs(y))

ans =

     0

y(y==0)=[];
min(abs(y))

ans =

    0.0078