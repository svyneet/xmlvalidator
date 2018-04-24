pipeline {
    agent any
    stages {
        stage('build'){

            steps{
                echo 'Preparing'
                sh 'python3 --version'
    			sh ('bash scripts/xmlvalidator.sh')
		     
		 }
		}
	   }
}

