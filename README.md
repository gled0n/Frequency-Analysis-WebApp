# Web Application for Frequency Analysis
![alt text](https://github.com/gled0n/Frequency-Analysis-WebApp/blob/master/graph_scr.PNG)
![alt text](https://github.com/gled0n/Frequency-Analysis-WebApp/blob/master/table_scr.png)

This work was developed as part of "PIN: Protection in Infrastructures and Networks Seminar" at Telecooperation Lab (TK) - Darmstadt Technical University in Summer term 2020.

Build the container:
```docker
docker build -f Dockerfile -t app:latest .
```

Run the container:
```docker
docker run -i -t -p 8501:8501 app:latest
```

The container is now available on http://localhost:8501/.
