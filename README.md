# NPL 
  control the motorized stage
  
  module file : <https://github.com/ken1row/PyOptoSigma>

  ## Specification
  OS : ubuntu 18.04

  Controller : SHOT-702
  
  Stage : [OSMS20-35(XY)](https://sihyunkorea.cafe24.com/product/osms20-35xy-m6-osms20-xy-%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%80/916/category/427/display/1/)

  ## Caution
  모듈이 Ubuntu로 작성되었기 때문에 defult OS는 Ubuntu 입니다. (Window에서 쓸 수 있게 수정할 예정)
  
  getkey 라이브러리를 사용해서 생기는 제약들이 있습니다.
  1. 반드시 sudo(관리자권한) 이어야 함 - 키보드 입력을 받기 때문에 보안 문제로 인해 sudo로 사용해야 함
  2. IDE 사용못함. 시스템 터미널을 사용할 것
     
  ## The needed functions
  1. reset the origin
  2. set a step size
  3. set a min/max pos
  4. python GUI (user interface)
  5. (If possible) Select the model of stage 1 and 2
  6. (If possible) Used in various models
