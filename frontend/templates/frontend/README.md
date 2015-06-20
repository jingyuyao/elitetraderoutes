# How templates are arranged

### Base templates

#### base.html

The mother of all templates.

#### detail\_base.html

Base of all model/detail.html

### Model templates

Templates for each model are listed in their own directories.

#### instance.html

This is the template used when a specific model instance is accessed.

Ex: localhost/model/1/

#### detail.html

This is used to just render the content of a specific model instance. It is factored out of instance.html so it can be reused.

##### thead.html

Used to construct the thead row of the model in a table.

##### row.html

The model as a row in a table.

#### list.html

This is used for the list view for a specific model

Ex: localhost/model/

#### form.html

This renders a form for a model. The action of the form is always pointed to the
list endpoint of the model since form only allows post data. When data=False is passed to it, it will *attempt* to render an empty form.
