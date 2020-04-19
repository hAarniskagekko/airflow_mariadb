FROM redis:6.0-rc-alpine

COPY redis.conf /data/

CMD redis-server /data/redis.conf

CMD tail -f /dev/null
