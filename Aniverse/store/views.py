from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from store.models import storage, Wishlist



def add_to_wishlist(request):
    if request.method == 'POST':
        # Assuming you're sending the product ID in the request data
        product_id = request.POST.get('productId')

        # Get the product based on the provided ID
        product = get_object_or_404(storage, id=product_id)

        # Get or create the user's wishlist
        wishlist = Wishlist.objects.get_or_create(user=request.user)[0]

        # Check if the product is already in the user's wishlist
        if product not in wishlist.products.all():
            # If not, add the product to the wishlist
            wishlist.products.add(product)
            return JsonResponse({'message': 'Added to Watchlist'}, status=200)
        else:
            return JsonResponse({'message': 'Anime already in Watchlist'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



