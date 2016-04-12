###
    Events
###

events = {}
events.sort_table = (list, attribute = 'data-sort-by') ->
    { onclick: (e) ->
        item = e.target.getAttribute(attribute)
        if item
            first = list[0]
            list.sort (a, b) ->
                if isNaN(parseFloat(a[item] * 1))
                    if isNaN(parseFloat(b[item] * 1))
                        if a[item] > b[item] then 1
                        else if b[item] > a[item] then -1
                        else 0
                    else -1
                else if isNaN(parseFloat(b[item] * 1)) then 1
                else if a[item] * 1 < b[item] * 1 then 1
                else if b[item] * 1 < a[item] * 1 then -1
                else 0
            if first == list[0]
                list.reverse()
        return
    }
events.delete_item = (list) ->
    {onclick: (e) ->
        console.log('*****************')
        index = e.target.getAttribute('index')
        for x,y in list
            console.log("x: " + x, "y: " + y, "index: " + index)
            if parseInt(index) == parseInt(y)
                list.splice(y,1)

        console.log("list: " + list)
    }

ROUTES = {
    "/": view: -> m.component(Home)
    "/home": view: -> m.component(Home)
    "/SignUp": view: -> m.component(CreateAccount)
    "/Login": view: -> m.component(LoginForm)
    "/meta": view: ->  m.component(RawEndpoint, {url: "data/amr"})
    "/gbrowse": view: -> m.component(GroupBrowse)
    "/groups": view: -> m.component(RawEndpoint, {url: "data/vf"})
    "/factors": view: -> m.component(Factors)
    "/results": view: -> mm.component(GeneResults)
}

add_route =  (func, route) ->
    ROUTES["/#{route}"] = view: -> m.component(func)

document.body.onload = ->
    for k, v of ROUTES
        console.log(k)
    m.route(document.body, "/", ROUTES)

#    "/": Home.get()
#    "/home": GroupBrowse.get()
#    "/meta": GroupBrowse.get()
#    "/gbrowse": GroupBrowse.get()
#    "/groups": UploadGenome.get()
#    "/factors": Factors.get()
#    "/results": GeneResults.get()
