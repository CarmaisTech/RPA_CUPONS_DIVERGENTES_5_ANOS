def estilo(sei):
    header_html = '''

                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                        <style>

                            *{
                                margin: 0;
                                padding: 0;
                            }
                            p{
                                text-transform: uppercase;
                                text-align: center;
                                font-size: 30px;
                                color: black;
                                margin-top: 15px

                            }
                            table{
                                position: relative;
                                width: 100%;
                                text-align: center;
                                text-transform: uppercase;
                                font-size: 12px;
                                border-collapse: collapse;
                                color: black;
                                border: none;
                                margin-bottom: 45px;
                                margin-top: 15px
                            
                            }
                            table thead{
                            border: 1px solid ;
                            background: #a5a5a5;
                            
                            }

                            table thead th{
                            padding: 6px;
                            border: none;
                            text-align: center;
                        
               
                            }
                            table tr{
                            font-size: 14px;
                        
                        
                            }
                            table td, td{
                            padding: 5px;
                            border: none;
                            text-align: center;
                            }
                            table tbody tr{
                           
                            
                            }
                           
                            table tbody tr:nth-child(2n+2){
                            background-color: rgb(194, 190, 190);
                            }
                            table tbody tr:last-of-type{
                            border-bottom: 2px solid aqua;

                            }
                            tbody tr:hover{
                              background: #C0C0C0;
                              cursor: pointer;
                            }
                           
                            hr{
                            margin-bottom: 25px;
                            }
                            
                        </style>
                    </head>
                 



        '''
    body_html = f'''
        <body>
                {sei}
        </body>
    '''

    return header_html + body_html
  