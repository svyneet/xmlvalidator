pipeline {
    agent any
    stages {
        stage('build'){

            steps{
                echo 'Preparing'
                sh 'python3 --version'
			dir ('scripts') { 
    				sh 'xmlvalidator.sh'
			}
		     
		 }
		}
	   }
}

