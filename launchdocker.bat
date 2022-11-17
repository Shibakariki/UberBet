docker-compose down
cd Dockerfile-Apache/
docker image build -t apache2_custom:alpha .
cd ../
cd Dockerfile-Redis/
docker image build -t redis_custom:alpha .
cd ../
cd Dockerfile-Postgres/
docker image build -t pg_custom:alpha .
cd ..
docker-compose up -d