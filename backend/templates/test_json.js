let amis = amisRequire('amis/embed');
amis.embed('#root', {
    type: 'page',
    title: 'Items Management',
    body: {
        type: 'crud',
        api: 'http://yourdomain.com/items',
        filter: {
            title: 'Search',
            submitText: '',
            controls: [
                {
                    type: 'text',
                    name: 'keyword',
                    placeholder: 'Search by keyword',
                    addOn: {
                        type: 'submit',
                        label: 'Search',
                        level: 'primary'
                    }
                }
            ]
        },
        columns: [
            {
                name: 'id',
                label: 'ID'
            },
            {
                name: 'name',
                label: 'Name'
            },
            {
                name: 'description',
                label: 'Description'
            },
            {
                type: 'operation',
                label: 'Operations',
                buttons: [
                    {type: 'button', label: 'Edit', actionType: 'dialog', dialog: {
                        title: 'Edit Item',
                        body: {
                            type: 'form',
                            api: 'put:http://yourdomain.com/items/${id}',
                            controls: [
                                {type: 'text', name: 'name', label: 'Name', required: true},
                                {type: 'textarea', name: 'description', label: 'Description'}
                            ]
                        }
                    }},
                    {type: 'button', label: 'Delete', actionType: 'ajax', confirmText: 'Are you sure you want to delete this item?', api: 'delete:http://yourdomain.com/items/${id}'}
                ]
            }
        ]
    }
});
