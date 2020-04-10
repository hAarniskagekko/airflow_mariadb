FROM redis:6.0-rc3

COPY /data/ redis.conf

RUN ./redis-server /data/redis.conf
