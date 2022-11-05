docker images --filter "dangling=true" -q > tmp
for /f "delims=" %%x in (tmp) do docker image rm %%x