- https://www.youtube.com/watch?v=PGyhBwLyK2U
- https://youtu.be/PGyhBwLyK2U?t=6088
- install the nodejs npm yarn 
- run yarn isntall 
- run yarn build
- serve -s build
---------------------------------------------------------
stages:
    - build
    - test
build website:
    image: node:16-alpine
    stage: build
    script:
        - yarn install
        - yarn build
    artifacts:
        paths:
            - build
test website:
    image: alpine
    stage: test
    script:
        - test -f build/index.html
unit tests:
    stage: test
    image: node:16-alpine
    script:
        - yarn install
        - yarn test
-------------------------------------------------------------------------------------