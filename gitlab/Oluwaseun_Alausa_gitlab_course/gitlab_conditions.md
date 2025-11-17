stages:
  stage_1:
    only:
      - master
    script:
      - echo "This job runs only on the master branch."
    stage_2:
        script:
            - echo "This job runs on all branches except develop."
if we have 10 stages to run only on main 
-----------------------------
workflow:
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: always (it is still under condition)
    - when: never (use this condition to stop all other branches)
    
