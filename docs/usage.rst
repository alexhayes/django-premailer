=====
Usage
=====

Use the ``premailer`` template tag around HTML where you need inline CSS:

.. code-block:: html

    {% load premailer %}

    {% premailer "http://example.com" %}
    <html>
    <style type="text/css">
    h1 { border:1px solid black }
    p { color:red;}
    .c {
      background-color: #FF6600;
    }
    .c td {
      background-color: #CCCCCC;
    }
    </style>
    <h1 style="font-weight:bolder">{{ eggs }}</h1>
    <p><a href="/blah/">Hej</a></p>
    <table class="c">
      <tr>
        <td></td>
      </tr>
    </table>
    </html>
    {% endpremailer %}

The rendered template would look as so;

.. code-block:: html

    <html>
    <head></head>
    <body>
        <h1 style="border:1px solid black; font-weight:bolder">Sausage</h1>
        <p style="color:red"><a href="http://example.com/blah/">Hej</a></p>
        <table style="background-color:#F60" bgcolor="#F60">
          <tr>
            <td style="background-color:#CCC" bgcolor="#CCC"></td>
          </tr>
        </table>
    </body>
    </html>

Settings
--------

If you need more control over premailer's init parameters you can define them using ``PREMAILER_OPTIONS``.

For example, in your settings file;

.. code-block:: python

    PREMAILER_OPTIONS = dict(base_url='http://example.com',
                             remove_classes=False)

See https://github.com/peterbe/premailer/blob/master/premailer/premailer.py#L149 for a list of other possible options.
