import System.IO

inputFile = "input.txt" :: [Char]

readLine :: Handle -> IO [String]
readLine handle = do
    eof <- hIsEOF handle
    if eof then return [] else do
        line <- hGetLine handle
        rest <- readLine handle
        return (line : rest)

readInput :: FilePath -> IO [String]
readInput path = do
    handle <- openFile path ReadMode
    lines <- readLine handle
    hClose handle
    return lines

concatenateDigits :: String -> Int
concatenateDigits line = 2 + 3

main :: IO()
main = do
    lines <- readInput inputFile
    print lines