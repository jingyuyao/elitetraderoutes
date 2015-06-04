# How templates are arranged

## *model*.html

This is the template used when a specific model instance is accessed.

Ex: localhost/model/1/

## *model*\_detail.html

This is used to just render the content of a specific model instance. It is factored out of
*model*.html so it can be reused.

## *model*\_list.html

This is used for the list view for a specific model

Ex: localhost/model/

## *model*\_form.html

This renders a form for a model. The action of the form is always pointed to the
list endpoint of the model since form only allows post data. When data=False is passed
to it, it will *attempt* to render an empty form.