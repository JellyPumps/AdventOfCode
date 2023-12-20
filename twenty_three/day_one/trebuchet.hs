import System.IO
import Data.Char (isDigit)
import Data.Maybe (catMaybes)

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

concatenateDigits :: String -> Maybe Int
concatenateDigits line =
    let digits = filter isDigit line
    in case digits of
        [] -> Nothing
        [x] -> Just (read [x,x])
        (x:xs) -> case reverse xs of
            [] -> Nothing
            (y:_) -> Just (read [x,y])

sumOfCalibration :: [Int] -> Int
sumOfCalibration = sum

main :: IO()
main = do
    lines <- readInput inputFile
    let maybeValues = map concatenateDigits lines
    let calibrationValues = catMaybes maybeValues
    let result = sumOfCalibration calibrationValues
    print result