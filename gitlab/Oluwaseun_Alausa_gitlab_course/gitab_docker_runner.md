- install gitlab on the server
- gitlab-runner register
  - Enter GitLab instance URL
  - Enter registration token
  - Enter description for the runner
  - Enter tags for the runner (comma-separated)
  - Enter executor type: docker
  - Enter default Docker image: (check dockerhub for newest docker image)
  Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
 
Configuration (with the authentication token) was saved in "/home/cloud_user_p_7e75c33b/.gitlab-runner/config.toml" 
- gitlab-runner start
- Verify runner is active in GitLab CI/CD settings
- To run jobs only on the main branch for 10 stages, use the following configuration in your .gitlab-ci.yml file:
-------------------------------------
# sample example
stages:
  - test
  - build
  - deploy
run_job:
  stage: test
  image: node:22-alpine
  tags:
    - docker
  before_script:
    - echo "This is run_job"
  script:
    - echo "This is script"
  after_script:
    - echo "Cleaning"
build_job:
  stage: build
  tags:
    - docker
  script:
    - echo "from build_jobs"
push_job:
  stage: build
  tags:
    - docker
  needs:
    - build_job
  script:
    - echo "from push job"
    