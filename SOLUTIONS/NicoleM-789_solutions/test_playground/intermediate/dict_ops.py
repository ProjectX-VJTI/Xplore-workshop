"""Practice common dictionary utilities."""


from typing import Any, Dict, Iterable




# swap keys and values
def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
   """Return value->key mapping."""
   return {v: k for k, v in d.items() }




# merge all dicts from left to right (latest key wins)
def merge_dicts(dicts: Iterable[Dict[Any, Any]]) -> Dict[Any, Any]:
   """Return a merged dict."""
   merged: Dict[Any, Any] = {}
   for chunk in dicts:
       for k, v in chunk.items():
         merged.update(chunk) #to keep the latest key-value pair
   return merged




# count keys that begin with a given prefix
def count_keys_with_prefix(d: Dict[str, Any], prefix: str) -> int:
   """Return number of keys that match prefix."""
   if not prefix:
       return len(d)       # returns total keys or 0 if prefix is empty
   return sum(1 for key in d if key.startswith(prefix))




if __name__ == "__main__":
   sample = {"pre_name": "A", "pre_age": 20, "city": "BLR"}
   print(invert_dict({"a": 1, "b": 2, 0: 7}))
   print(merge_dicts([{"x": 1}, {"y": 2}, {"x": 9}]))
   print(count_keys_with_prefix(sample, "pre_"))
