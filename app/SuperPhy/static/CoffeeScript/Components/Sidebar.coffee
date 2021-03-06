###
CLASS Sidebar

Component class for sidebar in VF and AMR feature

Args passed in:
    None yet

To do: Add components into Sidebar
###

class Sidebar
    @controller: (args) ->
        return @
    @view: (ctrl) ->
        m('.', {id: 'sidebar-wrapper'}, [
            m('.sidebar', [
                m('#sidebar-expand-collapse', [
                    m('button.btn btn-default[type=button]'
                        id: 'sidebar-expand'
                        ">>"
                    )
                    m('button.btn btn-default[type=button]'
                        id: 'sidebar-collapse'
                        "<<"
                    )
                ])
            ])
        ])