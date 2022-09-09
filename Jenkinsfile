pipeline {
    agent any
    parameters {
        string defaultValue: '', description: 'Nombre del usuario a crear', name: 'USUARIO', trim: true
        string defaultValue: '', description: 'contraseña nueva del usuario a crear', name: 'PASSWORD', trim: true
        choice choices: ['Lectura','Admin','Desarrollador'], description: '', name: 'TIPOUSUARIO'
        extendedChoice description: '', multiSelectDelimiter: ',', name: 'DATABASE', quoteValue: false, saveJSONParameterToFile: false, type: 'PT_CHECKBOX', 
            value: 'jenkinsdba', visibleItemCount: 10
    }
    environment {
        ADMINPERMISO = "SHOW DATABASES,INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER "
        DESARROLLADOR= "INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE,CREATE VIEW, CREATE ROUTINE, ALTER ROUTINE, TRIGGER"
        PERMISO = "SELECT, SHOW VIEW "
        SUFIJOHOST= "jenkinsdba.czy4ou9hlkg8.us-west-2.rds.amazonaws.com"
    }
    stages {
        stage ('Creando Usuario') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'mysql', passwordVariable: 'PASSWD_DB', usernameVariable: 'USER_DB')]) {
                        script {
                        def tipousuario="${TIPOUSUARIO}"
                        def browsers ="${DATABASE}".split(",")
                        if (browsers.size()>0){
                            if (tipousuario=="Admin"){
                                PERMISO= PERMISO +","+ ADMINPERMISO
                            }
                            if (tipousuario=="Desarrollador"){
                                PERMISO= PERMISO +","+ DESARROLLADOR
                            }
                            
                            for (int i = 0; i < browsers.size(); ++i) {
                                sh  "mysql -u${USER_DB} -p${PASSWD_DB} -h ${browsers[i]}.${SUFIJOHOST} -e \"CREATE USER IF NOT EXISTS '$USUARIO'@'%' IDENTIFIED BY '$PASSWORD' ;\""
                                sh  "mysql -u${USER_DB} -p${PASSWD_DB} -h ${browsers[i]}.${SUFIJOHOST} -e \"GRANT $PERMISO ON *.* TO '$USUARIO'@'%';\""
                            }
                        }
                    }
                }
            }
        }
    }
}
