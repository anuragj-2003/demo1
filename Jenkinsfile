pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python temp.py'
      }
    }
  }
}
