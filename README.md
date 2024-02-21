# NPL 
  control the motorized stage
  
  module file : <https://github.com/ken1row/PyOptoSigma>

  ## Specification
  OS : ubuntu 18.04

  Controller : SHOT-702
  
  Stage : [OSMS20-35(XY)](https://sihyunkorea.cafe24.com/product/osms20-35xy-m6-osms20-xy-%EC%8A%A4%ED%85%8C%EC%9D%B4%EC%A7%80/916/category/427/display/1/)

  ## Files
  beta_1.py : OSMS26-100 2개로 테스트할 때 사용한 코드 (in Ubuntu)

  beta_2.py : OSMS26-100 2개로 테스트할 때 사용한 코드 (in Window)

  ## Update
  https://www.reddit.com/r/learnpython/comments/yxfwy5/getkey_bug_in_vscode/
  
  2023.11.24 bug of Getkey on Windows. Getkey to keyboard

  ## Caution
  axis 1 : 위, 아래
  
  axis 2 : 좌, 우
  
  defult OS는 Ubuntu 입니다. (Window에서 쓰려면 포트를 지정해줘야 함)
  
  getkey 라이브러리를 사용해서 생기는 제약들이 있습니다.
  1. 반드시 sudo(관리자권한) 이어야 함 - 키보드 입력을 받기 때문에 보안 문제로 인해 sudo로 사용해야 함
  2. IDE 사용못함. 시스템 터미널을 사용할 것
  ## Manual
  (in Window)
  
  사전 준비

  install getkey, pyOptosigma, pyserial
  
  pip3 install pyOptosigma

  pip3 install getkey

  pip3 install pyserial
  
  default port : dev/ttyUSB0 <- 이게 우분투에서 기본 포트이기 때문에 따로 지정해줘야 함 (윈도우는 COMx 형식)

  == 포트 확인하는 법 ==
  
  장치관리자 -> 포트(COM & LPT) -> 포트확인
  
  ## The needed functions
  1. reset the origin - complete
  2. set a step size - complete
  3. set a min/max pos - complete
  4. Chek the code in Window OS
  5. (if possible)python GUI
