pipeline {
  environment {
    dockerimagename = "bobby/one-app"
    dockerImage = ""
  }
  agent any
  stages {
    stage('Checkout Source') {
        steps {
            checkout([$class: 'GitSCM', 
                      branches: [[name: '*/main']], 
                      doGenerateSubmoduleConfigurations: false, 
                      extensions: [], 
                      submoduleCfg: [], 
                      userRemoteConfigs: [[url: 'https://github.com/bobbyd234/jenkins-k8s-deployment.git']]])
        }
    }
    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build dockerimagename
        }
      }
    }
    stage('Pushing Image') {
      environment {
          registryCredential = 'dockerhub-credentials'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push("latest")
          }
        }
      }
    }
    stage('Deploying oneapp container to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "deployment.yaml", 
                                         "service.yaml")
        }
      }
    }

    stage('Deploy App on k8s') {
      steps {
        withCredentials([
            string(credentialsId: 'my_k8s', variable: 'api_token')
            ]) {
             sh 'kubectl --token $api_token --server http://127.0.0.1:51171/  --insecure-skip-tls-verify=true apply -f . '
               }
            }
}
        }
      
    }
  

