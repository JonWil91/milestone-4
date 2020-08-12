navbar taken and amended from Bootstrap

https://www.pinterest.co.uk/pin/10062799153143907/ - home page camera

products/views.py:

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

    copied from mini CI project


<!-- <div class="row mt-1 mb-2">
            <div class="col-12 col-md-6 my-auto order-md-last d-flex justify-content-center justify-content-md-end">
                <div class="sort-select-wrapper w-50">
                    <select id="sort-selector" class="custom-select custom-select-sm rounded-0 border border-{% if current_sorting != 'None_None' %}info{% else %}black{% endif %}">
                        <option value="reset" {% if current_sorting == 'None_None' %}selected{% endif %}>Sort by...</option>
                        <option value="price_asc" {% if current_sorting == 'price_asc' %}selected{% endif %}>Price (low to high)</option>
                        <option value="price_desc" {% if current_sorting == 'price_desc' %}selected{% endif %}>Price (high to low)</option>
                        <option value="rating_asc" {% if current_sorting == 'rating_asc' %}selected{% endif %}>Rating (low to high)</option>
                        <option value="rating_desc" {% if current_sorting == 'rating_desc' %}selected{% endif %}>Rating (high to low)</option>
                        <option value="name_asc" {% if current_sorting == 'name_asc' %}selected{% endif %}>Name (A-Z)</option>
                        <option value="name_desc" {% if current_sorting == 'name_desc' %}selected{% endif %}>Name (Z-A)</option>
                        <option value="category_asc" {% if current_sorting == 'category_asc' %}selected{% endif %}>Category (A-Z)</option>
                        <option value="category_desc" {% if current_sorting == 'category_desc' %}selected{% endif %}>Category (Z-A)</option>
                    </select>
                </div>
            </div>
            <div class="col-12 col-md-6 order-md-first">
                <p class="text-muted mt-3 text-center text-md-left">
                    {% if search_term or current_categories or current_sorting != 'None_None' %}
                        <span class="small"><a href="{% url 'products' %}">Products Home</a> | </span>
                    {% endif %}
                    {{ products|length }} Products{% if search_term %} found for <strong>"{{ search_term }}"</strong>{% endif %}
                </p>
            </div>
        </div> -->
taken from mini project

bag views copied from mini project, apart from if/else size arguments removed as all products have a size

checkout models.py, admin.py copied from mini project

https://compressjpeg.com/ used to compress images

pagination inspired by https://www.youtube.com/watch?v=N_TWOfLlc7A