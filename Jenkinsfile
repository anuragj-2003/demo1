pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'C:\\Users\\Anurag\\AppData\\Local\\Programs\\Python\\Python312\\python.exe --version'
      }
    }
    stage('hello') {
      steps {
        bat 'C:\\Users\\Anurag\\AppData\\Local\\Programs\\Python\\Python312\\python.exe temp.py'
      }
    }
  }
}
