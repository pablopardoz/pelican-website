# pablopardo.es

La primera prueba de mi web con pelican
scp -r /output root@vps347190.ovh.net/:/var/www


rsync -avzhe ssh pablo@vps347190.ovh.net/:/var/www /Users/pablo/blog/output
ssh-keygen -R vps347190.ovh.net

rsync -avc --delete output/ vps347190.ovh.net:/var/www/pardozaragoza.es/

<VirtualHost *:80>
        ServerAdmin     info@pardozaragoza.es
        ServerName      pardozaragoza.es
        ServerAlias     pardozaragoza.es
        DocumentRoot    /home/pablo/pardozaragoza.es/www/
        ErrorLog        /home/pablo/pardozaragoza.es/logs/error.log
        CustomLog       /home/pablo/pardozaragoza.es/logs/access.log combined

        <Directory />
                Options Indexes FollowSymLinks MultiViews
                AllowOverride All
                Order allow,deny
                allow from all
        </Directory>

</VirtualHost># pablopardo.es
