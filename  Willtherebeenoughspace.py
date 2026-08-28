def enough(cap, on, wait):
    return on+ wait - cap if on+ wait - cap > 0 else 0
 #   return max(0, on + wait - cap) // C'est des solutions proposes depuis codewars que j'ai decouvert cette methode max

print(enough(59, 46, 42)) 