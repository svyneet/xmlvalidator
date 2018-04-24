pipeline {
    agent any
    stages {
        stage('build'){

            steps{
                echo 'Preparing'
                sh 'python3 --version'
			cd scripts
			ls -lr
			sh ('bash xmlvalidator.sh')
		     
		 }
		}
	   }
}

