@REM cd Dockerfile-Apache/
@REM docker image build -t apache_custom:alpha .
@REM cd ../
cd Dockerfile-Python/
docker image build -t flask-app:alpha .
cd ..
cd Dockerfile-Postgres/
docker image build -t pg_custom:alpha .
cd ..
cd Dockerfile-MongoDB/
docker image build -t mongo_custom:alpha .
cd ..
docker-compose up