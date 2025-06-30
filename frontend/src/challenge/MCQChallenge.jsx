import "react";
import {useState} from "react";

// {
//     "content": "question",
//     "options": [1,2,3,4],
//     "correctAnswer": 0,
//     "explanation": "This is the explanation for the answer.",
// }

export function MCQChallenge(challenge, showExplanation = false) {
    const [selectedOption, setSelectedOption] = useState(null);
    const [shouldShowExplanation, setShouldShowExplanation] = useState(showExplanation);

    const options = typeof challenge.options === "string" ? JSON.parse(challenge.options) : challenge.options;

    const handleOptionChange = (index) => {
        if (selectedOption !== null) return;
        setSelectedOption(index);
        setShouldShowExplanation(true);
    }

    const getOptionClass = (index) => {
        if (selectedOption === null) return "option";
        if (index === challenge.correct_answer_id) return "correct option";
        if (index === selectedOption) return "incorrect option";
        return "option";
    }

    return <div className="challenge-display">
        <p><strong>Difficulty</strong>: {challenge.difficulty}</p>
        <p className="challenge-title">{challenge.title}</p>
        <div className="options">
            {options.map((option, index) => (
                <div className={getOptionClass(index)} key={index} onClick={() => handleOptionChange(index)}>
                    {option}
                </div>
            ))}
        </div>
        {shouldShowExplanation && selectedOption !== null && (
            <div className="explanation">
                <h4>Explanation</h4>
                <p>{challenge.explanation}</p>
            </div>
        )}
    </div>
}