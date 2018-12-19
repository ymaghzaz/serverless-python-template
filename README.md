# serverless-python-template

## Dependencies 
   - docker 
   - npm 
   - nodejs
   - serverless 
      ```js
      npm install  -g serverless
      ```

## Install
   
    
      git clone https://github.com/ysfmag/serverless-python-template.git
      cd serverless-python-template
      npm install
    
   
## Serverless

  - test localy : 
  ```js
    serverless invoke local -f hello -p test.json
  ```
  
  - test in aws : 
  ```js
    serverless invoke  -f hello -p test.json --stage dev  -r eu-west-1
  ```
  - deploy in aws : 
   ```js
    serverless deploy -r eu-west-1 --stage dev --verbose
   ```
