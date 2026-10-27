# Heapq Cheatsheet

## heapq.heapify(list)

Converts a regular list into a min-heap in-place.
Time Complexity = O(N)

---

## heapq.heappush(heap, item)

Pushes a new item onto the heap while maintaining heap invariant.
Time Complexity = \(O(\log N)\)

---

## heapq.heappop(heap)

Pops and returns the smallest element.
Time Complexity \(O(\log N)\)

---

## heap[0]

Peeks at the smallest element without removing it.
Time Complexity O(1)

---

## heapq.heappushpop(h, item)

Pushes item, then pops and returns the smallest element.
Time Complexity = \(O(\log N)\)

---

## heapq.heapreplace(h, item)

Pops the smallest element first, then pushes the new item.
Time Complexity = \(O(\log N)\)

---

## heapq.nsmallest(n, iterable)

Returns the n smallest elements from a dataset.
Time Complexity = \(O(N \log n)\)

---

## heapq.nlargest(n, iterable)

Returns the n largest elements from a dataset.
Time Complexity = \(O(N \log n)\)
