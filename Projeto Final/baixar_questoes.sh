#!/usr/bin/env bash

mkdir -p dados/questoes
curl 'https://vestibular.brasilescola.uol.com.br/simulado/questoes/' \
    -H 'Connection: keep-alive' \
    -H 'Cache-Control: max-age=0' \
    -H 'Upgrade-Insecure-Requests: 1' \
    -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36' \
    -H 'Origin: https://vestibular.brasilescola.uol.com.br' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' \
    -H 'Referer: https://vestibular.brasilescola.uol.com.br/simulado/questoes/' \
    -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
    -H 'Cookie: _ga=GA1.3.397043123.1551903937; chartbeat-related-content-3=default; PHPSESSID=c982vtgds83rjbe6uf1fn79er1' \
    --data 'disciplina_33=100000&disciplina_32=100000&disciplina_34=100000&disciplina_26=100000&disciplina_61=100000&disciplina_31=100000&disciplina_30=100000&disciplina_29=100000&disciplina_25=100000&disciplina_27=100000&disciplina_28=100000&disciplina_17=100000&disciplina_36=100000&disciplina_37=100000&disciplina_50=100000&disciplina_35=100000&disciplina_38=100000&disciplina_51=100000&disciplina_40=100000&disciplina_39=100000&disciplina_42=100000&disciplina_41=100000&disciplina_15=100000&disciplina_47=100000&disciplina_48=100000&disciplina_46=100000&disciplina_16=100000&disciplina_20=100000&disciplina_60=100000&disciplina_22=100000&disciplina_23=100000&disciplina_21=100000&disciplina_58=100000&disciplina_57=100000&disciplina_24=100000&disciplina_49=100000&disciplina_19=100000&disciplina_44=100000&disciplina_43=100000&disciplina_45=100000&disciplina_18=100000&btn_gerar=Gerar+Simulado' \
    --compressed > dados/_questoes.html
