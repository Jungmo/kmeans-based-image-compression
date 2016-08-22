# kmeans-based-image-compression

Inspired by ['K -Means Clustering-Based Data Compression Scheme for Wireless Imaging Sensor Networks'](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=7312938)


파일 모두에 적용하는 iteration 넣기 (O)

가끔씩 Centroid를 K보다 적게 선택하는 경우 해결 (O)

- 중복에 의한 문제였음.
  - centroid 배열의 길이로 했을 때 중복이 발생하면, centroid 배열의 element들을 dictionary의 key로 사용했을때
    문제가 발생한다.
  - 키가 중복되서, K보다 적은 key가 만들어진다.

##TODO
전송할 데이터로 압축.
