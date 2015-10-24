<<!DOCTYPE html>
<html>
  <head>
    <title>Hackita Froy Today in History</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/stylesheet.css" />
  </head>
  <body>
    <div>
      <div class='container'>
        <div class='calendar'>
          {{! calendar }}
          <p style="display:flex;">
              <a href="/{{past_year}}/{{past_month}}" class="nav">
                &lt;Previous Month
              </a>
              <a href="/{{next_year}}/{{next_month}}" class="nav">
                Next Month>
              </a>
          </p>
        </div>
      </div>
      %include('history.tpl')

  </body>
</html>
